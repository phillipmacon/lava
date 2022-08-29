// Copyright (C) 2021 Intel Corporation
// SPDX-License-Identifier: BSD-3-Clause
// See: https://spdx.org/licenses/

#ifndef MULTIPROCESSING_H_
#define MULTIPROCESSING_H_

#include <vector>
#include <functional>

#include "abstract_actor.h"
#include "shm.h"

namespace message_infrastructure {

class MultiProcessing {
 public:
  void Stop(bool block);
  int BuildActor(AbstractActor::TargetFn target_fn);
  void CheckActor();
  std::vector<AbstractActor::ActorPtr>& GetActors();

 private:
  std::vector<AbstractActor::ActorPtr> actors_;
};

}  // namespace message_infrastructure

#endif  // MULTIPROCESSING_H_

<<<<<<< HEAD
  std::vector<AbstractActor::ActorPtr> actors_;
=======
  std::vector<ActorPtr> actors_;
  int signal_key_ = 0xbee;
  SharedMemManager *shmm_;
};
